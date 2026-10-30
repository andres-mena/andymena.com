/* Progressive enhancement with Motion 14.9.0. Content is visible without JS. */
(() => {
  if (!window.Motion || !("IntersectionObserver" in window)) return;

  const { animateMini: animate, inView, stagger } = window.Motion;
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const printMode = window.matchMedia("print");
  const hoverAvailable = window.matchMedia("(hover: hover) and (pointer: fine)");
  const activeAnimations = new Set();
  const originalStyles = new Map();
  let cleanups = [];

  function play(elements, keyframes, options) {
    const targets = Array.from(elements);
    if (!targets.length || reducedMotion.matches || printMode.matches) return;
    for (const target of targets) {
      if (!originalStyles.has(target)) {
        originalStyles.set(target, target.getAttribute("style"));
      }
    }
    const controls = animate(targets, keyframes, options);
    activeAnimations.add(controls);
    Promise.resolve(controls).then(
      () => activeAnimations.delete(controls),
      () => activeAnimations.delete(controls),
    );
    return controls;
  }

  function reveal(elements, delay = 0) {
    return play(elements, { opacity: [0, 1], transform: ["translateY(14px)", "translateY(0px)"] }, {
      duration: 0.8,
      ease: [0.25, 0.1, 0.25, 1],
      delay,
    });
  }

  function reset() {
    cleanups.forEach((cleanup) => cleanup());
    cleanups = [];
    activeAnimations.forEach((controls) => controls.cancel());
    activeAnimations.clear();
    originalStyles.forEach((style, target) => {
      if (style === null) target.removeAttribute("style");
      else target.setAttribute("style", style);
    });
    originalStyles.clear();
  }

  function start() {
    reset();
    if (reducedMotion.matches || printMode.matches) return;

    reveal(document.querySelectorAll(".hero-copy > .eyebrow, .hero-copy > h1, .hero-copy > p"), stagger(0.06));
    reveal(document.querySelectorAll(".portrait img"), 0.12);

    const groups = [
      [".profile-links", "a", 0.04],
      [".policy-steps", "li", 0.18],
      [".paper-list", "li", 0.05],
    ];
    for (const [selector, children, interval] of groups) {
      cleanups.push(inView(selector, (group) => {
        reveal(group.querySelectorAll(`:scope > ${children}`), stagger(interval));
      }, { margin: "0px 0px -40px 0px" }));
    }

    cleanups.push(inView(
      ".policy-heading, .section-heading, .group-heading, .publication, .thesis-link, .course, .podcast-feature, .media-list > a, .footer",
      (element) => { reveal([element]); },
      { margin: "0px 0px -30px 0px" },
    ));

    if (hoverAvailable.matches) {
      document.querySelectorAll(".policy-steps li").forEach((card) => {
        const image = card.querySelector("img");
        let hoverAnimation;
        const move = (y) => {
          hoverAnimation?.stop();
          hoverAnimation = play([image], { transform: `translateY(${y}px)` }, {
            duration: 0.24,
            ease: [0.22, 1, 0.36, 1],
          });
        };
        const enter = () => move(-5);
        const leave = () => move(0);
        card.addEventListener("pointerenter", enter);
        card.addEventListener("pointerleave", leave);
        cleanups.push(() => {
          card.removeEventListener("pointerenter", enter);
          card.removeEventListener("pointerleave", leave);
        });
      });
    }
  }

  reducedMotion.addEventListener("change", start);
  printMode.addEventListener("change", start);
  start();
})();

document.addEventListener("DOMContentLoaded", function () {
  if (typeof MathJax !== "undefined") {
    MathJax.startup.promise.then(() => {
      MathJax.texReset();
      MathJax.typesetClear();
      MathJax.typesetPromise();
    });
  }
});

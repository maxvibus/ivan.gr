/* ivan.gr — ήπια κύλιση προς τα κείμενα και αναζήτηση στο ευρετήριο */
(function(){
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function ease(t){ return t<.5 ? 4*t*t*t : 1-Math.pow(-2*t+2,3)/2; }
  function glide(target){
    var start = window.scrollY, running = true;
    var end = Math.max(0, target.getBoundingClientRect().top + start - window.innerHeight*0.12);
    end = Math.min(end, document.documentElement.scrollHeight - window.innerHeight);
    if (reduce || Math.abs(end-start) < 2){ window.scrollTo(0,end); return; }
    var dur = 1500, t0 = null;
    ['wheel','touchstart','keydown','mousedown'].forEach(function(ev){ window.addEventListener(ev, function(){ running=false; }, {once:true, passive:true}); });
    function step(ts){ if(!running) return; if(t0===null) t0=ts; var p=Math.min(1,(ts-t0)/dur); window.scrollTo(0,start+(end-start)*ease(p)); if(p<1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a.down'); if(!a) return;
    var t = document.getElementById('texts'); if(!t) return; e.preventDefault(); glide(t);
  });
  function norm(s){ return (s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/ς/g,'σ'); }
  var inp = document.querySelector('.search input'); if(!inp) return;
  var none = document.querySelector('.none');
  inp.addEventListener('input', function(){
    var v = norm(inp.value.trim()), any = false;
    document.querySelectorAll('.year').forEach(function(g){
      var c = 0;
      g.querySelectorAll('li').forEach(function(li){ var ok = !v || li.getAttribute('data-k').indexOf(v) >= 0; li.hidden = !ok; if(ok) c++; });
      g.hidden = !c; if(c) any = true;
    });
    if(none) none.hidden = any;
  });
})();

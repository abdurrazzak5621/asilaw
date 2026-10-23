(function(){
  var root=document.documentElement;
  var DEF={theme:'night',font:'serif',width:'normal'};
  function load(){try{return JSON.parse(localStorage.getItem('cz-read'))||{};}catch(e){return {};}}
  function save(){try{localStorage.setItem('cz-read',JSON.stringify(S));}catch(e){}}
  var S=load();
  function apply(){
    root.setAttribute('data-theme',S.theme||DEF.theme);
    root.setAttribute('data-font',S.font||DEF.font);
    root.setAttribute('data-width',S.width||DEF.width);
    root.style.setProperty('--fs',(S.fs||19)+'px');
  }
  function $(s,c){return (c||document).querySelector(s);}
  function $$(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s));}

  /* reading settings panel */
  var btn=$('#cz-aa'),panel=$('#cz-panel');
  function sync(){
    $$('[data-set]').forEach(function(b){var k=b.getAttribute('data-set');b.setAttribute('aria-pressed',String((S[k]||DEF[k])===b.getAttribute('data-val')));});
    var o=$('#cz-fs');if(o){o.textContent=(S.fs||19)+'px';}
  }
  function close(focus){if(panel&&!panel.hidden){panel.hidden=true;btn.setAttribute('aria-expanded','false');if(focus){btn.focus();}}}
  if(btn&&panel){
    btn.addEventListener('click',function(e){e.stopPropagation();var opening=panel.hidden;panel.hidden=!opening;btn.setAttribute('aria-expanded',String(opening));});
    panel.addEventListener('click',function(e){
      e.stopPropagation();
      var b=e.target.closest?e.target.closest('button'):null;if(!b){return;}
      var k=b.getAttribute('data-set');if(k){S[k]=b.getAttribute('data-val');}
      var d=b.getAttribute('data-fs');if(d){S.fs=Math.max(15,Math.min(26,(S.fs||19)+parseInt(d,10)));}
      apply();save();sync();
    });
    document.addEventListener('click',function(){close(false);});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'){close(true);}});
    sync();
  }

  var latestMeta=document.querySelector('meta[name="cz-latest"]');
  var latest=latestMeta?parseInt(latestMeta.content,10):0;
  var base=document.querySelector('.brand').getAttribute('href');

  /* chapter page: progress bar, keys, remember position */
  var art=$('.reader[data-ch]');
  if(art){
    var n=parseInt(art.getAttribute('data-ch'),10);
    S.last={n:n,t:art.getAttribute('data-name')};save();
    var body=$('#post-body'),bar=$('#cz-progress');
    if(bar&&body){
      var onScroll=function(){var r=body.getBoundingClientRect();var total=Math.max(1,body.offsetHeight-window.innerHeight*0.55);var p=Math.min(1,Math.max(0,(80-r.top)/total));bar.style.width=(p*100).toFixed(2)+'%';};
      window.addEventListener('scroll',onScroll,{passive:true});window.addEventListener('resize',onScroll);onScroll();
    }
    document.addEventListener('keydown',function(ev){
      if(ev.altKey||ev.ctrlKey||ev.metaKey||ev.shiftKey){return;}
      var tg=(ev.target&&ev.target.tagName)||'';if(/^(INPUT|TEXTAREA|SELECT)$/.test(tg)){return;}
      var a=null;
      if(ev.key==='ArrowLeft'){a=$('.cn-prev[href]');}
      if(ev.key==='ArrowRight'){a=$('.cn-next[href]');}
      if(a){location.href=a.href;}
    });
  }

  /* home: continue where you left off */
  var lb=$('#cz-latest');
  if(lb&&S.last&&S.last.n&&latest){
    var next=S.last.n+1;
    if(next<=latest){lb.href=base+'chapter/'+next+'.html';lb.textContent='Continue with Chapter '+next;}
  }
  /* chapter list: mark where the reader is */
  if(S.last&&S.last.n){
    $$('.ch-rows.compact .ch-row a').forEach(function(a){
      if(/chapter\/(\d+)\.html$/.exec(a.getAttribute('href'))&&parseInt(RegExp.$1,10)===S.last.n){a.parentNode.className+=' is-last';a.setAttribute('aria-label','Last read: '+a.textContent);}
    });
  }
})();

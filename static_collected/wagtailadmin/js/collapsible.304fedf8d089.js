(()=>{"use strict";var e,t={3023:function(e,t,o){var r=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};t.__esModule=!0;var n=r(o(73609));function l(){n.default(".object.collapsible").each((function(){var e=n.default(this),t=e.find(".object-layout"),o=function(){return t.get(0).dispatchEvent(new CustomEvent("commentAnchorVisibilityChange",{bubbles:!0}))};e.hasClass("collapsed")&&0===e.find(".error-message").length&&t.hide({complete:o}),e.find("> .title-wrapper").on("click",(function(){e.hasClass("collapsed")?(e.removeClass("collapsed"),t.show({duration:"slow",complete:o})):(e.addClass("collapsed"),t.hide({duration:"slow",complete:o}))}))}))}window.initCollapsibleBlocks=l,n.default((function(){l()}))},73609:e=>{e.exports=jQuery}},o={};function r(e){var n=o[e];if(void 0!==n)return n.exports;var l=o[e]={id:e,loaded:!1,exports:{}};return t[e].call(l.exports,l,l.exports,r),l.loaded=!0,l.exports}r.m=t,e=[],r.O=(t,o,n,l)=>{if(!o){var a=1/0;for(d=0;d<e.length;d++){for(var[o,n,l]=e[d],i=!0,s=0;s<o.length;s++)(!1&l||a>=l)&&Object.keys(r.O).every((e=>r.O[e](o[s])))?o.splice(s--,1):(i=!1,l<a&&(a=l));i&&(e.splice(d--,1),t=n())}return t}l=l||0;for(var d=e.length;d>0&&e[d-1][2]>l;d--)e[d]=e[d-1];e[d]=[o,n,l]},r.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return r.d(t,{a:t}),t},r.d=(e,t)=>{for(var o in t)r.o(t,o)&&!r.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})},r.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),r.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),r.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),r.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.j=778,(()=>{var e={778:0};r.O.j=t=>0===e[t];var t=(t,o)=>{var n,l,[a,i,s]=o,d=0;for(n in i)r.o(i,n)&&(r.m[n]=i[n]);if(s)var u=s(r);for(t&&t(o);d<a.length;d++)l=a[d],r.o(e,l)&&e[l]&&e[l][0](),e[a[d]]=0;return r.O(u)},o=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];o.forEach(t.bind(null,0)),o.push=t.bind(null,o.push.bind(o))})(),r.O(void 0,[751],(()=>r(3023)));var n=r.O(void 0,[751],(()=>r(90971)));n=r.O(n)})();
//# sourceMappingURL=collapsible.js.a41e9a298154.map
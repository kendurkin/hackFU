window.onload=function(){
    var t = new Trianglify({cellsize: 40});
    var pattern = t.generate(document.body.clientWidth,document.body.clientHeight);
    document.body.setAttribute('style','background-image:'+pattern.dataUrl+';background-size: cover;background-attachment: fixed');
}


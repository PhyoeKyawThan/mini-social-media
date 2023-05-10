let post_btn = document.getElementById('post-btn');
let post_section = document.getElementById('post-section');
let post_form = document.getElementById('post-form');
let upload    = document.getElementById('upload-btn');
let images = document.querySelectorAll('img');
var view = document.getElementById('view');
var imgSrc = view.querySelector('img');

images.forEach((img)=>{
    img.onload = ()=>{
        var imgHeight = img.naturalHeight;
        if(imgHeight > 768){
            img.style.margin = '-50% auto';
        }
        getSrc(img);
    }
});

var getSrc = (image)=>{
    image.addEventListener('click', (e)=>{
        imgSrc.src = e.target.src;
        post_section.style.display = 'none';
        document.querySelector('.img-view').style.display = 'block';
    })
    
}

let back = document.querySelector('.back');
back.addEventListener('click', ()=>{
    post_section.style.display = 'block';
    document.querySelector('.img-view').style.display = 'none';

});

post_btn.addEventListener('click', ()=>{
    if(post_form.style.display === 'none'){
    post_form.style.display = 'block';
    }else{
        post_form.style.display = 'none';
    }
})

upload.addEventListener('click', ()=>{
    post_form.style.display = 'none';
})
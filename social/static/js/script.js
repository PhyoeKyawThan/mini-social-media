let post_btn = document.getElementById('post-btn');
let post_section = document.getElementById('post-section');
let post_form = document.getElementById('post-form');
let upload    = document.getElementById('upload-btn');
let images = document.querySelectorAll('img');


images.forEach((img)=>{
    img.onload = ()=>{
        var imgHeight = img.naturalHeight;
        if(imgHeight > 768){
            img.style.margin = '-50% auto';
        }
        getAlt(img);
    }
});

var getAlt = (image)=>{
    image.addEventListener('click', (e)=>{
        console.log(e.target.src);
    })
}

post_btn.addEventListener('click', ()=>{
    post_form.style.display = 'block';
    post_btn.style.display  = 'none';
})

upload.addEventListener('click', ()=>{
    post_form.style.display = 'none';
})
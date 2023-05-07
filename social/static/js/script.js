let post_btn = document.getElementById('post-btn');
let post_section = document.getElementById('post-section');
let post_form = document.getElementById('post-form');
let upload    = document.getElementById('upload-btn');

post_btn.addEventListener('click', ()=>{
    post_form.style.display = 'block';
    post_btn.style.display  = 'none';
})

upload.addEventListener('click', ()=>{
    post_form.style.display = 'none';
})
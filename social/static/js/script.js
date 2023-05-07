let post_btn = document.getElementById('post-btn');
let post_section = document.getElementById('post-section');
let post_form = document.getElementById('post-form');


post_btn.addEventListener('click', ()=>{
    post_form.style.display = 'block';
    post_btn.style.display  = 'none';
})
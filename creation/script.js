let image = document.querySelector(".img-view");
let img = document.querySelector(".img");
let post = document.querySelector('.posts');
img.addEventListener('click', (e)=>{
    image.style.display = 'block';
    post.style.display   = 'none';
});
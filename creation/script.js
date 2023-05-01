const post = document.getElementById("post");
const profile = document.getElementById("profile");
let form = document.getElementById("post-form");
let post_section = document.getElementById("posts");
post.addEventListener("click", ()=>{
    form.style.display = "none";
    post_section.style.display = 'block';
});

profile.addEventListener("click", ()=>{
    form.style.display = "block";
    post_section.style.display = 'none';
});
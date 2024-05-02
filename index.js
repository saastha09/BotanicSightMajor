// const nav = document.querySelector(".nav"),
//   searchIcon = document.querySelector("#searchIcon"),
//   navOpenBtn = document.querySelector(".navOpenBtn"),
//   navCloseBtn = document.querySelector(".navCloseBtn");

// searchIcon.addEventListener("click", () => {
//   nav.classList.toggle("openSearch");
//   nav.classList.remove("openNav");
//   if (nav.classList.contains("openSearch")) {
//     return searchIcon.classList.replace("uil-search", "uil-times");
//   }
//   searchIcon.classList.replace("uil-times", "uil-search");
// });

// navOpenBtn.addEventListener("click", () => {
//   nav.classList.add("openNav");
//   nav.classList.remove("openSearch");
//   searchIcon.classList.replace("uil-times", "uil-search");
// });
// navCloseBtn.addEventListener("click", () => {
//   nav.classList.remove("openNav");
// });

// // 
// const imageInput = document.getElementById('imageInput'); 
     
// imageInput.addEventListener('change', (event) => { 
//   const file = event.target.files[0]; 
//   // Perform further processing with the selected image file 
//   console.log(file); 
// }); 


function classifyImage() {
  const fileInput = document.getElementById('imageInput');
  const file = fileInput.files[0];

  const formData = new FormData();
  formData.append('image', file);

  fetch('http://127.0.0.1:5000/classify', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('result').innerText = `Class: ${data.classification}`;
  })
  .catch(error => console.error('Error:', error));
}

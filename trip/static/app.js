document.addEventListener("DOMContentLoaded", function(){
  const editBtn =document.querySelector("#editBtn");
  console.log(editBtn.innerHTML);
  if(editBtn.innerHTML === "Completed Trip"){
    editBtn.disabled = true;
  }
});
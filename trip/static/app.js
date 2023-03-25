document.addEventListener("DOMContentLoaded", function(){
  const editBtn =document.querySelector("#editBtn");
  const addTripBtn = document.querySelector("#add_trip");

  
  console.log(editBtn.innerHTML);
  if(editBtn.innerHTML === "Completed Trip" || editBtn.innerHTML==="Requested Trip"){
    editBtn.display = "None";
  }else{
    console.log(editBtn.innerHTML);
  }

  console.log(addTripBtn.innerHTML);

  // handle login form
  const username = document.querySelector("#username");
  console.log(username.value);
  const password = document.querySelector("#password");
  console.log(password.value);

});
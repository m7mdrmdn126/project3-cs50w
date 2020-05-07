document.addEventListener('DOMContentLoaded', () =>{
  document.querySelector('#register').onclick = () => {
    document.querySelector('#in-use').style.left = "95px";
    document.querySelector('#register-form').style.left = "10px";
    document.querySelector('#login-form').style.left = "-400px";
    document.querySelector('.forms').style.height = "450px";
  };
  document.querySelector('#login').onclick = () => {
    document.querySelector('#in-use').style.left = "0";
    document.querySelector('#register-form').style.left = "450px";
    document.querySelector('#login-form').style.left = "10px";
    document.querySelector('.forms').style.height = "380px;";
  }
})

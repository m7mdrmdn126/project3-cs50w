document.addEventListener('DOMContentLoaded', () => {
    var pizza = document.querySelector('#pizza-selector');
    console.log(pizza.value)

   pizza.onchange = () => {
    
    // this topic get topping list from the server then it make atopping list if 
    // we want it

    if (pizza.value != "chesee" && pizza.value != "None"){
        const request = new XMLHttpRequest();
        request.open('POST', '/toppin')
        request.setRequestHeader("X-CSRFToken", csrf)

        request.onload = () => {

            const data =JSON.parse(request.responseText); 
            
            let del = document.querySelector('.topp_select');
           

            if(del === null){
                var topp_select = document.createElement("select");
                topp_select.className = "topp_select";
                topp_select.name = "topping";
                data.forEach(topp => {
                var opt = document.createElement('option');
                opt.value = topp;
                opt.text = topp; 
                topp_select.add(opt);
                });
            

            document.querySelector('#topp').append(topp_select);

        }

            };
        request.send();
        return false;

        }
    else{
        let del = document.querySelector('.topp_select');
        if (del != null){
            document.querySelector('#topp').removeChild(del);
        } 
    }
       

   }


   // adding menus to alist
   var menu_list = []
   document.querySelectorAll('.menu').forEach(men =>{
        menu_list.push(men)
   })

   // setting the menu we will display 
   var n_menu = 0
   console.log(menu_list)


   var nav_menu = []
   // adding the headers where we can navigate betwwen menus
   document.querySelectorAll('.menu-nav').forEach(nv =>{
        nav_menu.push(nv)
    })
    console.log(nav_menu)


    // leave it for a while

    // arrows
    document.querySelector("#right-arrow").onclick = () => {
        destroing()
        if (n_menu < menu_list.length - 1){
            n_menu += 1
        }
        else{
            n_menu = 0;
        }
        menu_list[n_menu].style.display = "block";
        nav_menu[n_menu].style.color = "#fdcb6e";

    }


    document.querySelector("#left-arrow").onclick = () => {
        destroing()
        if (n_menu > 0){
            n_menu -= 1
        }
        else{
            n_menu =  menu_list.length - 1;
        }
        menu_list[n_menu].style.display = "block";
        nav_menu[n_menu].style.color = "#fdcb6e";

    }







    destroing()
    nav_menu[n_menu].style.color = "#fdcb6e";
    menu_list[n_menu].style.display = "block";


   // frontend things :)

   function destroing () {
       document.querySelectorAll('.menu').forEach(men =>{
        men.style.display = "none";
       })

        document.querySelectorAll('.menu-nav').forEach(nv =>{
        nv.style.color = "white";
        
    })
   }

   function ev_destroing(){
        document.querySelector('#menu').style.display = "none";
        document.querySelector('#order_forms').style.display = "none";
        document.querySelector('#cart').style.display = "none";
   }

   ev_destroing()
   document.querySelector('#menu').style.display = "block";

   document.querySelector('#mn').onclick = () => {
    ev_destroing()
    document.querySelector('#menu').style.display = "block";

   }

   document.querySelector('#od').onclick = () => {
    ev_destroing()
    document.querySelector('#order_forms').style.display = "block";
       
    }

    document.querySelector('#cr').onclick = () => {
        ev_destroing()
        document.querySelector('#cart').style.display = "block";
        
    }
   







   




});
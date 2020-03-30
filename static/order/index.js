document.addEventListener('DOMContentLoaded', () => {
    var pizza = document.querySelector('#pizza-selector');
    console.log(pizza.value)

   pizza.onchange = () => {

    if (pizza.value != "chesee" && pizza.value != "None"){
        const request = new XMLHttpRequest();
        request.open('POST', '/toppin')
        request.setRequestHeader("X-CSRFToken", csrf)

        request.onload = () => {

            const data =JSON.parse(request.responseText); 
            
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



});
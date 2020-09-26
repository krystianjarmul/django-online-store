var updateBtns = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function() {
        let productId = this.dataset.product;
        let action = this.dataset.action;

        console.log('PRODUCT_ID:', productId, 'ACTION:', action);

        if(user === 'AnonymousUser'){
            console.log("Not logged in")
        }
        else{
            console.log("User is logged in, sending data...")
        }

        console.log('USER:', user);
    })
}
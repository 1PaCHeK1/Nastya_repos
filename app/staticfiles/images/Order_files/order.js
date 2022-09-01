function downolad_order() {
    order = localStorage.getItem('order')
    if (order === null){ order = [] }
    else { order = JSON.parse(order) }

    return order
}

function change_button(product_id) {
    btn = document.getElementById('product_' + product_id)
    if(btn!==null)
    {
        btn.onclick = () => window.open('/order/');
        btn.textContent = "В корзину";
    }
}

function init_order() {
    let order = downolad_order();
    for (const index in order) {
        change_button(order[index].product_id);
    }
}


function append_in_order(product_id) {
    
    let order = downolad_order();
    
    let containt = false;

    for (const index in order) {
        if(product_id == order[index].product_id){
            order[index].amount += 1
            containt = true;
            break
        }
    }
    
    if(!containt) {
        order.push({
            product_id: product_id,
            amount: 1
        })
    } 
    console.log(order)
    localStorage.setItem('order', JSON.stringify(order))
    change_button(product_id)
}

function pop_in_order(product_id) {
    for (const index in order) {
        if(product_id == order[index].product_id){
            if(order[index].amount == 1){
                order.pop(index)
            }
            else {
                order[index].amount -= 1
            }
            break
        }
    }
    localStorage.setItem('order', JSON.stringify(order))
    console.log(order)
}


function template_product(product) {
    return `
    <div class="card" style="width: 18rem; float: left; margin-left: 30px;">
        <a href='/product/${product.id}'>  
            <img src="{% static 'images/default-product-image.png' %}" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">${product.name}</h5>
            <p class="card-text">${product.description}</p>
            </div>
        </a>
        <button id="product_in_order_${product.id}" onclick="append_in_order(${product.id});" class="btn btn-outline-danger">+1</button>
        <button id="product_in_order_${product.id}" onclick="pop_in_order(${product.id});" class="btn btn-outline-danger">-1</button> 
    </div>
    `
}

init_order()
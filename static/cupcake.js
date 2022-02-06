// alert ('im here')

const $cupcakeFlavor = $("[name='flavor']")
const $cupcakeSize = $("[name='size']")
const $cupcakeRating = $("[name='rating']")
const $cupcakeImage = $("[name='image']")
const $createCupcakeBtn = $('#create-cupcake')
const $cupcakeForm = $('form')

async function handleCreateEvt(evt) {
    console.log('clicked')
    evt.preventDefault()
    
    cupcake = {
        flavor: $cupcakeFlavor.val(),
        size: $cupcakeSize.val(),
        rating: $cupcakeRating.val(),
        image : $cupcakeImage.val()
    }
    res = await axios.post('/api/cupcakes', cupcake)
    console.log(res)
}

$createCupcakeBtn.on('click', handleCreateEvt);

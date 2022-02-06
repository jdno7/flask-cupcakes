// alert ('im here')

const $cupcakeFlavor = $("[name='flavor']")
const $cupcakeSize = $("[name='size']")
const $cupcakeRating = $("[name='rating']")
const $cupcakeImage = $("[name='image']")
const $createCupcakeBtn = $('#create-cupcake')
const $cupcakeForm = $('form')


async function listCupcakes (evt){
   res = await axios.get('/api/cupcakes')

}

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


for (let cupcake of res.data.cupcakes){
    const $cupcakesList = $('#cupcakes-list')
    const $li = $(`<li><a href=/cupcakes/${cupcake.id}>${cupcake.flavor}</a></li>`)
    $cupcakesList.append($li)
}

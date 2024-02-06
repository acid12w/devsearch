

let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')


// if(alertWrapper) {
//   alertClose.forEach(element => {
//     element.addEventListener('click', function(e) {
//       console.log(e)
//     })
//   })
// }


// if(alertWrapper) {
//   console.log('wrapper clicked')
//   alertWrapper.addEventListener('click', function(e) {
//     console.log('inside wrapper clicked')
//     // alertWrapper.getElementsByClassName.display = 'none'
//     })
//   }

const myInterval = setInterval(function myTimer() {

  alertWrapper.style.display = 'none'
}, 1000);



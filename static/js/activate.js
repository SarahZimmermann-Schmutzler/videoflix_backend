
// import Cookies from 'js-cookie';
// let Cookies = require('js-cookie')

// let token = Cookies.get('csrftoken');


// window.onload=async function(){
    
//     let url = window.location.href;
//     let url_string = url.toString();
//     let url_parts = url_string.split('/');
//     let encoded_pk = url_parts[4];
//     let myData = {
//         'encoded_pk': encoded_pk
//     };
    
//     try{
//         let PatchRequest = await fetch(
//             'account_activation/',
//             {
//                 method: 'PATCH',
//                 credentials: "same-origin",
//                 headers: {
//                     "X-CSRFToken": token,
//                     "Accept": "application/json",
//                     "Content-Type": "application/json"
//                 },
//                 body: JSON.stringify(myData)
//             }).then(function(response) {
//                 return response.json();
//             }).then(function(data) {
//                 console.log("Data is ok", data);
//             });
//     } catch (e) {
//         console.error('An error occured', e)
//     }
// }
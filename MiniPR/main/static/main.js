// $(document).ready(function () {
//     listup_car();
//     listup_malibu();
// });

//     function listup_car() {
//     $.ajax({
//         type: "GET",
//         url: "/car",
//         data: {},
//         success: function (response) {
//             let rows = response['cars']
//             for (let i = 0; i < rows.length; i++) {
//                 let carname = rows[i]['carname']
//                 let image = rows[i]['image']
//                 let index = rows[i]['index']
//                 let type = rows[i]['type']

//                 console.log(carname, image, index, type)
//             }
//         }
//     })
// }



// function malibu() {
//     $.ajax({
//         type: "GET",
//         url: "/main/car",
//         data: {},
//         success: function (response) {

//             let rows = response['cars']

//             for (let i = 0; i < rows.length; i++) {
//                 let carname = rows[i]['carname']
//                 let image = rows[i]['image']
//                 let index = rows[i]['index']
//                 let type = rows[i]['type']

//                 console.log(carname, image, index, type)
//             }
//         }
//     })
// }

// function malibu() {
//     $.ajax({
//         type: "GET",
//         url: "/main/car",
//         data: {},
//         success: function (response) {
//             console.log(response)
//         }
//     });
// }
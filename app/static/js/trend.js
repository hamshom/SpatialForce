// console.log("loaded trend.js");

var trendTableData = [{
    "zipcode": "94704",
    "count": 789
  },
  {
    "zipcode": "94889",
    "count": 456
  },
  {
    "zipcode": "92979",
    "count": 123
  }
];

displayResult(trendTableData);

function displayResult(data){
  for(let i=0; i<data.length;i++){
    $("#trendTable").append(`<tr class="new">
      <td>${data[i].zipcode}</td>
      <td>${data[i].count}</td>
    </tr>`)
  }
};



// // convert string to JSON
// var response = trendTableData;
// console.log("loaded the jsonfile");
// console.log(response);
//
// $(function() {
//     $.each(response, function(i, item) {
//         var $tr = $('<tr>').append(
//             $('<td>').text(item.zipcode),
//             $('<td>').text(item.count)
//         ); //.appendTo('#records_table');
//         console.log($tr.wrap('<p>').html());
//     });
// });


//
// $(document).ready(function() {
//   // Handler for .ready() called.
//   $("body").on('mouseenter', ()=>{
//     $("#trendTable").append('<tr><td>my data</td><td>more data</td></tr>');
//   })
// });

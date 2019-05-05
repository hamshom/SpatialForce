console.log("loaded rank.js");

var rankData = {
  "pop": {
    "top": [90123, 90124, 90125, 90126, 90127],
    "bottom": [99123, 99124, 99125, 99126, 99127]
  },
  "edu": {
    "top": [91123, 91124, 91125, 91126, 91127],
    "bottom": [98123, 98124, 98125, 98126, 98127]
  },
  "income": {
    "top": [92123, 92124, 92125, 92126, 92127],
    "bottom": [97123, 97124, 97125, 97126, 97127]
  },
  "house": {
    "top": [93123, 93124, 93125, 93126, 93127],
    "bottom": [96123, 96124, 96125, 96126, 96127]
  }
}

// displayResult(rankData);
//
// function displayResult(data) {
//   console.log(data['race']);
//   var selected = "race";
//   for (let i = 0; i < data[selected]['top'].length; i++) {
//     $("#list_top").append(`<li>${data[selected]['top'][i]}</li>`)
//   }
// };

// Population
$("#rank-btn-pop").on('click', function() {
  var data = rankData;
  var selected = 'pop';
  $("#list_top").html("Top 5:");
  $("#list_bottom").html("Bottom 5:");
  for (let i = 0; i < data[selected]['top'].length; i++) {
    $("#list_top").append(`<li class="list-group-item">${data[selected]['top'][i]}</li>`)
  }
  for (let i = 0; i < data[selected]['bottom'].length; i++) {
    $("#list_bottom").append(`<li class="list-group-item">${data[selected]['bottom'][i]}</li>`)
  }
});

// EDUCATION
$("#rank-btn-edu").on('click', function() {
  var data = rankData;
  var selected = 'edu';
  $("#list_top").html("Top 5:");
  $("#list_bottom").html("Bottom 5:");
  for (let i = 0; i < data[selected]['top'].length; i++) {
    $("#list_top").append(`<li class="list-group-item">${data[selected]['top'][i]}</li>`)
  }
  for (let i = 0; i < data[selected]['bottom'].length; i++) {
    $("#list_bottom").append(`<li class="list-group-item">${data[selected]['bottom'][i]}</li>`)
  }
});

// INCOME
$("#rank-btn-income").on('click', function() {
  var data = rankData;
  var selected = 'income';
  $("#list_top").html("Top 5:");
  $("#list_bottom").html("Bottom 5:");
  for (let i = 0; i < data[selected]['top'].length; i++) {
    $("#list_top").append(`<li class="list-group-item">${data[selected]['top'][i]}</li>`)
  }
  for (let i = 0; i < data[selected]['bottom'].length; i++) {
    $("#list_bottom").append(`<li class="list-group-item">${data[selected]['bottom'][i]}</li>`)
  }
});

// HOUSE
$("#rank-btn-house").on('click', function() {
  var data = rankData;
  var selected = 'house';
  $("#list_top").html("Top 5:");
  $("#list_bottom").html("Bottom 5:");
  for (let i = 0; i < data[selected]['top'].length; i++) {
    $("#list_top").append(`<li class="list-group-item">${data[selected]['top'][i]}</li>`)
  }
  for (let i = 0; i < data[selected]['bottom'].length; i++) {
    $("#list_bottom").append(`<li class="list-group-item">${data[selected]['bottom'][i]}</li>`)
  }
});

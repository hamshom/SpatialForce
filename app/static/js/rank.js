// console.log("loaded rank.js");

// var rankData = {
//   "pop": {
//     "top": [90123, 90124, 90125, 90126, 90127],
//     "bottom": [99123, 99124, 99125, 99126, 99127]
//   },
//   "edu": {
//     "top": [91123, 91124, 91125, 91126, 91127],
//     "bottom": [98123, 98124, 98125, 98126, 98127]
//   },
//   "income": {
//     "top": [92123, 92124, 92125, 92126, 92127],
//     "bottom": [97123, 97124, 97125, 97126, 97127]
//   },
//   "house": {
//     "top": [93123, 93124, 93125, 93126, 93127],
//     "bottom": [96123, 96124, 96125, 96126, 96127]
//   }
// }

$(document).ready(function() {
  $('#rank-btn-pop').on('click', function() {
    $.ajax({
        data: {
          type: "pop"
        },
        type: 'POST',
        url: '/rank'
      })
      .done(function(data) {
        if (data.error) {
          $('.list-group-item').children().hide();
          console.log(data.error);
        } else {
          for (let i = 0; i < 5; i++) {
            $('#list_item0' + i).text(data['top'][i]).show();
            $('#list_item1' + i).text(data['bottom'][i]).show();
          }
          console.log(data);
        }
      });
    event.preventDefault();
  });

  $('#rank-btn-edu').on('click', function() {
    $.ajax({
        data: {
          type: "edu"
        },
        type: 'POST',
        url: '/rank'
      })
      .done(function(data) {
        if (data.error) {
          $('.list-group-item').children().hide();
          console.log(data.error);
        } else {
          for (let i = 0; i < 5; i++) {
            $('#list_item0' + i).text(data['top'][i]).show();
            $('#list_item1' + i).text(data['bottom'][i]).show();
          }
          console.log(data);
        }
      });
    event.preventDefault();
  });

  $('#rank-btn-income').on('click', function() {
    $.ajax({
        data: {
          type: "income"
        },
        type: 'POST',
        url: '/rank'
      })
      .done(function(data) {
        if (data.error) {
          $('.list-group-item').children().hide();
          console.log(data.error);
        } else {
          for (let i = 0; i < 5; i++) {
            $('#list_item0' + i).text(data['top'][i]).show();
            $('#list_item1' + i).text(data['bottom'][i]).show();
          }
          console.log(data);
        }
      });
    event.preventDefault();
  });

  $('#rank-btn-house').on('click', function() {
    $.ajax({
        data: {
          type: "house"
        },
        type: 'POST',
        url: '/rank'
      })
      .done(function(data) {
        if (data.error) {
          $('.list-group-item').children().hide();
          console.log(data.error);
        } else {
          for (let i = 0; i < 5; i++) {
            $('#list_item0' + i).text(data['top'][i]).show();
            $('#list_item1' + i).text(data['bottom'][i]).show();
          }
          console.log(data);
        }
      });
    event.preventDefault();
  });
});

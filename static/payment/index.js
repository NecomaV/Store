var stripe = Stripe('pk_test_51L1ZxxAEgKCl1oTaO7l6YF0zKYExtW1maKcOPdsg5yZm7gvKho8ImGlkkmBPPtbyuRSl0DapjS7ggX0IA9kNoPB800JNNi0knE')

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');


var elements = stripe.elements();
var style = {
base: {
  color: "#000",
  lineHeight: '2.4',
  fontSize: '16px'
}
};


var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function(event) {
var displayError = document.getElementById('card-errors')
if (event.error) {
  displayError.textContent = event.error.message;
  $('#card-errors').addClass('alert alert-info');
} else {
  displayError.textContent = '';
  $('#card-errors').removeClass('alert alert-info');
}
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
ev.preventDefault();

var custName = document.getElementById("custName").value;
var custSurname = document.getElementById("custSurname").value;
var custNumber = document.getElementById("custNumber").value;
var custAdd = document.getElementById("custAdd").value;
var custCountry = document.getElementById("custCountry").value;
var custCity = document.getElementById("custCity").value;
var postCode = document.getElementById("postCode").value;
var custComments = document.getElementById("custComments").value;


      stripe.confirmCardPayment(clientsecret, {
        payment_method: {
          card: card,
          billing_details: {
            address:{
                line1:custAdd,
            },
            name: custName,
            surname: custSurname,
            number: custNumber,
            country: custCountry,
            city: custCity,
            postCode: postCode,
            comments: custComments

          },
        }
      }).then(function(result) {
        if (result.error) {
          console.log('payment error')
          console.log(result.error.message);
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            console.log('payment processed')
            window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
          }
        }
      });
    })

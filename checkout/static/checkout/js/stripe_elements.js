/* Code adapted from Stripe documentation:
https://stripe.com/docs/payments/accept-a-payment 
*/

var stripePublicKey = $(`#id_stripe_public_key`).text().slice(1,-1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
      color: "#545454",
      fontSmoothing: "antialiased",
      fontSize: "15px",
      fontFamily: '"Karla", Helvetica, sans-serif',
      "::placeholder": {
        color: "#545454"
      }
    },
    invalid: {
      color: "#dc3545",
      iconColor: "#dc3545"
    }
  };
var card = elements.create("card", { style: style });
// Stripe injects an iframe into the DOM
card.mount("#card-element");

//Validation errors on card element
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
    var html = `
      <span>${event.error.message}</span>
    `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = '';
  }
});

//Checkout form submit
var form = document.getElementById('checkout-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ 'disabled': true });
  $('#submit-button').attr('disabled', true);
  $('#submit-button').fadeToggle(100);
  $('#loading-button').fadeToggle(100);

  var saveDetails = Boolean($('#id-save-details').attr('checked'));
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_details': saveDetails,
  };
  var url = '/checkout/cache_checkout_data/';

  $.post(url, postData).done(function() {
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            email: $.trim(form.email.value),
            address:{
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                state: $.trim(form.county.value),
            }
        }
    },
    shipping: {
        name: $.trim(form.full_name.value),
        phone: $.trim(form.phone_number.value),
        address: {
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.town_or_city.value),
            country: $.trim(form.country.value),
            postal_code: $.trim(form.postcode.value),
            state: $.trim(form.county.value),
        }
    },
    }).then(function(result) {
      if (result.error) {
        var errorDiv = document.getElementById('card-errors');
        var html = `
            <span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        $('#submit-button').fadeToggle(100);
        $('#loading-button').fadeToggle(100)
        card.update({ 'disabled': false });
        $('#submit-button').attr('disabled', false);
      } else {
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
  }).fail(function () {
    location.reload();
  })
});

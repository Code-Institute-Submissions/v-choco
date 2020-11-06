/* Code adapted from Stripe documentation:
https://stripe.com/docs/payments/accept-a-payment 
*/

var stripe_public_key = $(`#id_stripe_public_key`).text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
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

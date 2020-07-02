<template>
  <div id="cart">
    <h3>Cart</h3>
    <div v-if="Object.keys(cart_object).length !== 0">
      <ul>
        <li v-for="(value, key, index) in cart_object">
          <div class="cart-item-container">
            <div class="cart-item">{{key}}</div>
            <div class="amount">
              <button :disabled="sub_is_disabled[index]" @click="subOne(key)">-</button>
              x{{value.amount}}
              <button @click="addOne(key)">+</button>
              <button class="delete-button" @click="removeFromCart(key)"><i class="fa fa-close"></i>
              </button>
            </div>
          </div>
        </li>
        <li>
          <div class="cart-item-container"  style="color: gray">
            <div class="cart-item">
              Delivery
            </div>
            <div class="amount">
              {{ delivery_price }}$
            </div>
          </div>
        </li>
      </ul>
      <hr>
      <div class="cart-item-container">
        <div class="cart-item">
          Total in
          <label>
            <input type="radio" name="currency" value="USD" v-model="currency" checked>
            USD
          </label>
          <label>
            <input type="radio" name="currency" value="EUR" v-model="currency">
            EUR
          </label>
          :
        </div>
        <div class="amount">
          <div v-if="currency === 'USD'">
            {{ total }}$
          </div>
          <div v-else>
            {{ total_in_euros }}€
          </div>
        </div>
      </div>
      <br>
      <button @click="showModal = true">
        ORDER NOW
      </button>
      <order-form v-if="showModal" @close="showModal = false">
      </order-form>
    </div>
    <p v-else>Your cart is empty. Add items from the menu</p>

  </div>
</template>

<script>
import axios from 'axios';
import OrderForm from './OrderForm';

export default {
  components: {
    OrderForm,
  },

  data() {
    return {
      showModal: false,
      currency: 'USD',
      eurToUsd: 0,
      delivery_price: 5,
    };
  },

  computed: {
    cart_object() {
      return this.$store.state.cart;
    },

    sub_is_disabled() {
      const { cart } = this.$store.state;
      const keys = Object.keys(cart);

      return keys.map((item) => {
        if (cart[item].amount > 1) {
          return false;
        }
        return 'disabled';
      });
    },

    total() {
      const { cart } = this.$store.state;
      let total = 0;
      Object.keys(cart).forEach((key) => {
        total += cart[key].price * cart[key].amount;
      });
      total += this.delivery_price;
      return total.toFixed(2);
    },

    total_in_euros() {
      return (this.total * this.eurToUsd).toFixed(2);
    },

  },

  methods: {

    addOne(cartItem) {
      this.$store.commit('addOne', cartItem);
    },

    subOne(cartItem) {
      this.$store.commit('subOne', cartItem);
    },

    removeFromCart(item) {
      this.$store.commit('removeFromCart', item);
    },
  },
  created() {
    axios.get('https://api.exchangeratesapi.io/latest?base=USD&symbols=EUR').then((r) => {
      this.eurToUsd = r.data.rates.EUR;
    });
  },

};
</script>
<style>

  #cart {
    width: 300px;
    position: fixed;
    right: 10px;
    top: 20%;
    padding: 10px;
    background: #ffe;
    border: 1px solid #333;
  }

  .cart-item-container {
    text-align: left;
    display: table;
    width: 100%;
  }

  .amount {
    text-align: right;
    display: table-cell;
  }

  .cart-item {
    text-align: left;
    display: table-cell;
  }

  .delete-button {
    background-color: transparent;
    border: 0;
  }

  .delete-button:hover {
    color: red;
  }
</style>

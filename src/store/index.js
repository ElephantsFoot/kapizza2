import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    cart: {},
  },
  mutations: {
    addToCart(state, item) {
      if (state.cart.hasOwnProperty(item.name)) {
        Vue.set(state.cart[item.name], 'amount', ++state.cart[item.name].amount);
      } else {
        Vue.set(state.cart, item.name, {});
        Vue.set(state.cart[item.name], 'amount', 1);
        Vue.set(state.cart[item.name], 'price', item.price);
      }
    },
    addOne(state, cartItem) {
      Vue.set(state.cart[cartItem], 'amount', ++state.cart[cartItem].amount);
    },
    subOne(state, cartItem) {
      Vue.set(state.cart[cartItem], 'amount', --state.cart[cartItem].amount);
    },
    removeFromCart(state, cartItem) {
      Vue.delete(state.cart, cartItem);
    },
    clearCart(state) {
      Vue.set(state, 'cart', {});
    },
  },
});

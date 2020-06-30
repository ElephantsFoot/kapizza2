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
        Vue.set(state.cart, item.name, ++state.cart[item.name]);
      } else {
        Vue.set(state.cart, item.name, 1);
      }
    },
    addOne(state, cartItem) {
      Vue.set(state.cart, cartItem, ++state.cart[cartItem]);
    },
    subOne(state, cartItem) {
      Vue.set(state.cart, cartItem, --state.cart[cartItem]);
    },
    removeFromCart(state, cartItem) {
      Vue.delete(state.cart, cartItem);
    },
  },
});

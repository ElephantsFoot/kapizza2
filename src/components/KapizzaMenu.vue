<template>
  <div id="menu">
    <div class="pizza" v-for="p in pizzas">
      <img class="menu-img" :src="pizzaImage(p.img_url)" alt="pizza photo">
      <h4>{{ p.name }}</h4>
      <div class="description">
        {{p.description}}
      </div>
      <br>
      <button @click="addToCart(p)">
        ADD TO CART
      </button>
      {{p.price}}$
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {

  data() {
    return {
      pizzas: [],
    };
  },

  methods: {

    pizzaImage(imgUrl) {
      try {
        return require(`../assets/menu_photos/${imgUrl}.jpg`);
      } catch (e) {
        return '';
      }
    },

    addToCart(item) {
      this.$store.commit('addToCart', item);
    },
  },

  created() {
    axios.get('/api/pizzas').then((r) => {
      this.pizzas = r.data.pizzas;
    });
  },
};
</script>

<style>
  .menu-img {
    display: block;
    height: 200px;
    width: 300px;
    margin-left: auto;
    margin-right: auto;
  }

  .pizza {
    border: 1px solid black;
    margin: 10px;
    width: 400px;
    max-height: 350px;
    height: 350px;
    text-align: left;
    padding: 10px;
    display: inline-block;
    vertical-align:top;
  }
</style>

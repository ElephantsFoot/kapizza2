<template>
  <div id="app">
    <cart></cart>
    <kapizza-menu></kapizza-menu>
  </div>
</template>

<script>
import Cart from './components/Cart';
import KapizzaMenu from './components/KapizzaMenu';

export default {
  components: {
    Cart, KapizzaMenu,
  },

  name: 'app',

  data() {
  },
};
</script>

<style>
</style>

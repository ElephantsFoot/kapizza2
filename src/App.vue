<template>
  <div id="app">
    <header>
      <div class="header-content">
        <div class="header-row">
          <img class="header-picture" :src="kapizzaImg" alt="science" style="float: left">
          <h1 class="company-name"> KaPizza</h1>
          <p class="motto"><i>We deliver even to the freakin' moon</i></p>
        </div>
      </div>
    </header>
    <main>
      <kapizza-menu></kapizza-menu>
    </main>
    <cart></cart>
    <footer>
      <p>Made by Elisha Damsker&ensp;
        <a href="https://github.com/ElephantsFoot/kapizza2">
          <i class="fa fa-github fa-lg">
          </i>
        </a>&ensp;
        <a href="mailto:el.damsker@gmail.com">
          <i class="fa fa-at fa-lg">
          </i>
        </a>
      </p>
    </footer>
  </div>
</template>

<script>
import Cart from './components/Cart';
import KapizzaMenu from './components/KapizzaMenu';

const kapizzaImg = require('./assets/kapizza_header.jpg');

export default {
  components: {
    Cart, KapizzaMenu,
  },

  name: 'app',

  data() {
    return {
      kapizzaImg,
    };
  },
};
</script>

<style>
  header {
    padding: 10px;
    text-align: center;
    background: #1abc9c;
    color: white;
    font-size: 20px;
  }

  footer {
    padding: 10px;
    text-align: center;
    background: darkslategray;
    color: white;
    font-size: 14px;
  }

  .header-content {
    display: table;
    width: 100%;
    height: 100%;
  }

  .header-row {
    display: table-row;
  }

  .header-picture {
    display: table-cell;
    vertical-align: middle;
    width: 33%;
  }

  .company-name {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
    width: 33%;
  }

  .motto {
    text-align: center;
    display: table-cell;
    vertical-align: middle;
    width: 33%;
  }

  main {
    margin: 0 auto;
    width: 1000px;
  }
</style>

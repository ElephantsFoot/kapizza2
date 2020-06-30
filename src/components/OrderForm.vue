<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container">
        <button class="delete-button" @click="$emit('close')"><i class="fa fa-close"></i></button>
        <form @submit.prevent="placeOrder()">
          First name<input type="text" required v-model="first_name"><br>
          Last name<input type="text" required v-model="last_name"><br>
          Phone number<input type="text" required v-model="phone_number"><br>
          Address<input type="text" required v-model="address"><br>
          <input type="submit" value="SUBMIT">
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'OrderForm',
  data() {
    return {
      first_name: '',
      last_name: '',
      phone_number: '',
      address: '',
    };
  },
  methods: {
    placeOrder() {
      const body = {
        first_name: this.first_name,
        last_name: this.last_name,
        phone_number: this.phone_number,
        address: this.address,
        ...this.$store.state,
      };
      axios.post('/api/place_order', body);
      this.$emit('close');
    },
  },
};
</script>

<style scoped>
  .modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: table;
    transition: opacity 0.3s ease;
  }

  .modal-wrapper {
    display: table-cell;
    vertical-align: middle;
  }

  .modal-container {
    width: 300px;
    margin: 0 auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    transition: all 0.3s ease;
    font-family: Helvetica, Arial, sans-serif;
  }

  .delete-button {
    float: right;
  }
</style>

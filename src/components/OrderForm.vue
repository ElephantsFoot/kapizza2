<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container">
        <button class="delete-button" @click="$emit('close')"><i class="fa fa-close"></i></button>
        <form @submit="$emit('close')">
          First name<input type="text" required><br>
          Last name<input type="text" required><br>
          Phone number<input type="text" required><br>
          Address<input type="text" required><br>
          <input type="submit" value="SUBMIT">
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderForm',
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

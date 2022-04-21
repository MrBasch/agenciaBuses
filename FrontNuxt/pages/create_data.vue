<template>
  <h1>{{ msg }}</h1>
</template>

<script>
export default {
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    async createData() {
      await fetch(`http://127.0.0.1:8000/back/create_data`, {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) => res.json().then((data) => (this.msg = data.message)));
    },
  },
  created() {
    this.createData();
  },
};
</script>

<style>
</style>
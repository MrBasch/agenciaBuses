<template>
  <v-dialog max-width="500px" v-model="open">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Add City</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter city name"></v-text-field>
        <v-text-field v-model="code" label="Enter city code"></v-text-field>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click.stop="saveCity(name, code)" color="#417D7A">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "createBusModal",
  props: ["open"],
  data() {
    return {
      name: "",
      code: "",
      state: "",
      status: ["AVAILABLE", "ON_THE_WAY", "UNAVAILABLE", "ON_REPAIR"],
    };
  },
  methods: {
    async saveCity(name, code) {
      await fetch(`http://127.0.0.1:8000/back/city?code=${code}&name=${name}`, {
        method: "POST",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) => res.json().then((data) => console.log(data)));
    },
  },
};
</script>
<style scoped>
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
.cardTitle {
  background-color: #1a3c40;
}
</style>
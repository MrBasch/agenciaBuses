<template>
  <v-dialog max-width="500px" v-model="edit">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Update or create city</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter city name"></v-text-field>
        <v-text-field v-model="code" label="Enter city code"></v-text-field>
        <v-text-field
          v-model="new_code"
          label="Enter city new_code"
        ></v-text-field>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click.stop="updateCity(name, code, new_code)" color="#417D7A"
          >Update</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "updateBusModal",
  props: ["edit"],
  data() {
    return {
      code: "",
      name: "",
      new_code: "",
      state: "",
      status: ["AVAILABLE", "ON_THE_WAY", "UNAVAILABLE", "ON_REPAIR"],
    };
  },
  methods: {
    async updateCity(name, code, new_code) {
      await fetch(
        `http://127.0.0.1:8000/back/city?code=${code}&name=${name}&new_code=${new_code}`,
        {
          method: "PUT",
          mode: "cors",
          headers: {
            Authorization: `Token ${localStorage.token}`,
          },
          cache: "default",
        }
      ).then((res) => res.json().then((data) => console.log(data)));
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
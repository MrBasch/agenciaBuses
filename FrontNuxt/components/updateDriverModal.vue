<template>
  <v-dialog max-width="500px" v-model="edit">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Update or create Driver</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter driver name"></v-text-field>
        <v-text-field v-model="rut" label="Enter old driver rut"></v-text-field>
        <v-text-field
          v-model="new_rut"
          label="Enter new driver rut"
        ></v-text-field>
        <v-select
          v-model="state"
          :items="status"
          label="Select a state"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="
            updateDriver(
              (name = name),
              (rut = rut),
              (new_rut = new_rut),
              (status = state)
            )
          "
          color="#417D7A"
          >Update</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "updateDriverModal",
  props: ["edit"],
  data() {
    return {
      name: "",
      rut: "",
      new_rut: "",
      state: "",
      status: ["AVAILABLE", "ON_THE_WAY", "UNAVAILABLE"],
    };
  },
  methods: {
    async updateDriver(name, rut, new_rut, status) {
      await fetch(
        `http://127.0.0.1:8000/back/driver?status=${status}&name=${name}&rut=${rut}&new_rut=${new_rut}`,
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
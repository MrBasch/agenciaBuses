<template>
  <v-dialog max-width="500px" v-model="open">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Add Bus</v-card-title>
      <v-form>
        <v-text-field v-model="code" label="Enter bus code"></v-text-field>
        <v-select
          v-model="state"
          :items="status"
          label="Select A Status"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="saveBus((code = code), (status = state))"
          color="#417D7A"
          >Add</v-btn
        >
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
      code: "",
      state: "",
      status: ["AVAILABLE", "ON_THE_WAY", "UNAVAILABLE", "ON_REPAIR"],
    };
  },
  methods: {
    async saveBus(code, status) {
      await fetch(
        `http://127.0.0.1:8000/back/bus?code=${code}&status=${status}`,
        {
          method: "POST",
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
</style>
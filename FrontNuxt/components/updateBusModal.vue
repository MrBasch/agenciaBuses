<template>
  <v-dialog max-width="500px" v-model="edit">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Update or create bus</v-card-title>
      <v-form>
        <v-text-field v-model="code" label="Enter bus code"></v-text-field>
        <v-text-field
          v-model="new_code"
          label="Enter the new bus code"
        ></v-text-field>
        <v-select
          v-model="state"
          :items="status"
          label="Select A Status"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="
            updateBus((code = code), (status = state), (new_code = new_code))
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
  name: "updateBusModal",
  props: ["edit"],
  data() {
    return {
      code: "",
      new_code: "",
      state: "",
      status: ["AVAILABLE", "ON_THE_WAY", "UNAVAILABLE", "ON_REPAIR"],
    };
  },
  methods: {
    async updateBus(code, status, new_code) {
      await fetch(
        `http://127.0.0.1:8000/back/bus?code=${code}&status=${status}&new_code=${new_code}`,
        {
          method: "PUT",
          mode: "cors",
          headers: {
            Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
          },
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
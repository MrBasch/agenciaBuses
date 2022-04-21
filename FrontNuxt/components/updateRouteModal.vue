<template>
  <v-dialog max-width="500px" v-model="edit">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Update or create Route</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter name"></v-text-field>
        <v-text-field v-model="code" label="Enter code"></v-text-field>
        <v-text-field v-model="new_code" label="Enter new code"></v-text-field>
        <v-select
          multiple
          v-model="stations_selected"
          :items="stations"
          label="Select stations"
        ></v-select>
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
            updateRoute(name, code, new_code, stations_selected, state)
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
  name: "updateRouteModal",
  props: ["edit"],
  data() {
    return {
      name: "",
      code: "",
      new_code: "",
      state: "",
      stations_selected: [],
      stations: [],
      routes: [],
      status: ["AVAILABLE", "CLOSED", "UNAVAILABLE"],
    };
  },
  methods: {
    async updateRoute(name, code, new_code, list_stations, state) {
      await fetch(
        `http://127.0.0.1:8000/back/route?code=${code}&new_code=${new_code}&name=${name}&stops=${list_stations}&status=${state}`,
        {
          method: "PUT",
          mode: "cors",
          headers: {
            Authorization: `Token ${localStorage.token}`,
          },
          cache: "default",
        }
      ).then((res) =>
        res.json().then((data) => {
          console.log(data);
          this.edit = !this.edit;
        })
      );
    },
    async getStations() {
      await fetch("http://127.0.0.1:8000/back/station", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          data.map((station) => this.stations.push(station.name));
        })
      );
    },
  },
  created() {
    this.getStations();
  },
};
</script>
<style scoped>
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
</style>
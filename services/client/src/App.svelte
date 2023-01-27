<script>
	import Header from "./components/Header.svelte";
	const api_path = "http://localhost:5000/api";

	let userQuery = "2278880688";
	let userFound = { found: false, id: "", name: "" };
	function fetchUser() {
		fetch(api_path + `/user/${userQuery}`)
			.then((res) => res.json())
			.then((data) => {
				console.log(data);
				if (data.id === undefined) {
					throw new Error("User not found");
				}
				userFound = { found: true, id: data.id, name: data.name };
			})
			.catch((err) => {
				console.log(err);
				userFound = { found: false, id: "", name: "" };
			});
	}

	let playlistList = [];
	function getUserPlaylists() {
		fetch(api_path + `/user/${userFound.id}/playlists`)
			.then((res) => res.json())
			.then((data) => {
				console.log(data);
				if (data.length === 0) {
					throw new Error("No playlists found");
				}
				if (data[0].title === undefined || data[0].title === undefined) {
					throw new Error("Response is not valid");
				}
				playlistList = data;
			})
			.catch((err) => {
				console.log(err);
				playlistList = [];
			});
	}

	function downloadPlaylist(playlist) {
		fetch(api_path + `/playlist/${playlist.id}/download`)
			.then((res) => res.json())
			.then((data) => {
				console.log(data);
			});
	}
</script>

<div style="margin:10px 20px 0 20px">
	<Header />
	<div style="display:flex; justify-content: space-between;">
		<div>
			<h2>User</h2>
			<input bind:value={userQuery} />
			<button on:click={fetchUser}>Search user</button>
			{#if userFound.found}
				<span style="color:green">User {userFound.name} found</span>
			{:else}
				<span style="color:brown">User not found</span>
			{/if}
		</div>

		<div>
			<h2 style="text-align: right;">Playlists</h2>
			{#if userFound.found}
				<button on:click={getUserPlaylists}>Show user playlists</button>
			{:else}
				<button
					style="cursor: not-allowed; pointer-events: none; background-color:#5d5d5d ;"
					>Show user playlists</button
				>
			{/if}
		</div>
	</div>

	<div
		style="display:flex;flex-wrap: wrap;gap:12px;justify-content: space-between;"
	>
		{#each playlistList as playlist}
			<div style="display:flex;flex-direction: column; align-items:center;">
				<h3 style="text-align: center;">{playlist.title}</h3>
				<button
					style="width: 100px;"
					on:click={() => {
						downloadPlaylist(playlist);
					}}>Download</button
				>
			</div>
		{/each}
	</div>
</div>

<script>
	let userQuery = "";
	function fetchUser() {
		fetch(`https://api.github.com/users/${userQuery}`)
			.then((res) => res.json())
			.then((data) => {
				console.log(data);
				resultList = [data.login || "Not found"];
			});
	}
	let resultList = [];
</script>

<input type="text" bind:value={userQuery} />
<button on:click={fetchUser}>Search user</button>

{#if resultList.length > 0}
	<ul>
		{#each resultList as result}
			<li>{result}</li>
		{/each}
	</ul>
{/if}

<script lang="ts">
	import { Content, Header, Panel } from '@smui-extra/accordion';
	import IconButton, { Icon } from '@smui/icon-button';
	import List, { Item, Meta, Label } from '@smui/list';
	import Checkbox from '@smui/checkbox';
	import { createEventDispatcher } from 'svelte';
	import Dialog, { Title, Content as DiaContent, Actions } from '@smui/dialog';
	import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';

	// const dispatch = createEventDispatcher()

	export let label: string;
	export let open: boolean = false;
	export let content: any[] = [];
	let suggestion: string = '';
	let modalOpen = false;

	export let activeTab: string;
	// interface CheckBoxStates {
	//     [key: string]: boolean;
	// }
	// export let checkBoxStates: CheckBoxStates;

	const suggestionProperties = tweened(
		{ leftPercOffset: 0, topOffset: 0, scale: 1, opacity: 0 },
		{ duration: 400, easing: cubicOut }
	);

	async function handleClick(prompt: string) {
		console.log('click');
		const result = await fetch('https://htn.onrender.com/suggestion', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				note: prompt
			})
		})
			.then((res) => {
				return res.json();
			})
			.then(async (data) => {
				console.log(data);
				suggestion = data.suggestion;
				suggestionProperties.set({
					...$suggestionProperties,
					topOffset: -70,
					leftPercOffset: 50,
					opacity: 1
				});
				setTimeout(() => {
					suggestionProperties.set({ leftPercOffset: 0, topOffset: 0, scale: 1, opacity: 0 });
				}, 4000);
			});
	}
</script>

<Panel bind:open variant="unelevated">
	<Header>
		{label}
		<IconButton slot="icon" toggle pressed={open}>
			<Icon class="material-icons" on>expand_less</Icon>
			<Icon class="material-icons">expand_more</Icon>
		</IconButton>
	</Header>
	<Content>
		{#if content.length == 0}
			<div class="text-sm text-gray-500">No sub tasks</div>
		{/if}

		<!-- <Dialog
  bind:modalOpen
  aria-labelledby="simple-title"
  aria-describedby="simple-content"
>
  <Title id="simple-title">Suggestion</Title>
  <DiaContent id="simple-content">Super awesome dialog body text?</DiaContent>
</Dialog> -->

		{#if $suggestionProperties.opacity > 0}
			<div
				style={`left: ${$suggestionProperties.leftPercOffset}%; transform: translate(-${$suggestionProperties.leftPercOffset}%, calc(-50% + ${$suggestionProperties.topOffset}px)) scale(${$suggestionProperties.scale}); opacity: ${$suggestionProperties.opacity}`}
				class="z-30 max-w-full absolute left-0 top-1/2 -translate-y-1/2"
			>
				<div
					class="mx-2 py-4 px-2 rounded-xl text-white bg-[#e499ff] whitespace-nowrap text-ellipsis overflow-hidden"
				>
					{suggestion}
				</div>
			</div>
		{/if}

		<List>
			{#each content as item}
				<Item class="flex justify-between" on:click={() => handleClick(item)}>
					<Label>{item}</Label>
					<button>
						<span class="material-icons">settings_suggest</span>
					</button>
				</Item>
			{/each}
		</List>
	</Content>
</Panel>

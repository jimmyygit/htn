<script lang="ts">
	import Tab, { Label } from '@smui/tab';
	import TabBar from '@smui/tab-bar';
	import Accordion from '@smui-extra/accordion';
	import Button from '@smui/button';
	import { Input } from '@smui/textfield';
	import SubcategoryPanel from '$lib/components/SubcategoryPanel.svelte';
	import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';

	interface Subcategory {
		[key: string]: { content: string[]; open: boolean };
	}

	let categories: { [key: string]: Subcategory } = {
		Tasks: {
			Shopping: { content: ['eggs', 'tomatoes'], open: false },
			Homework: { content: ['eggs', 'tomatoes'], open: false },
			General: { content: ['eggs', 'tomatoes'], open: false }
		},
		Goals: {
			Personal: { content: ['eggs', 'tomatoes'], open: false },
			Career: { content: ['eggs', 'tomatoes'], open: false }
		},
		Notes: {
			Ideas: { content: ['eggs', 'tomatoes'], open: false },
			'For later': { content: ['eggs', 'tomatoes'], open: false }
		}
	};
	let tabs = Object.keys(categories);
	let activeTab = tabs[0];

	let note = '';
	let noteCopy = '';
	const noteProperties = tweened(
		{ leftPercOffset: 0, topOffset: 0, scale: 1, opacity: 0 },
		{ duration: 400, easing: cubicOut }
	);

	function sleep(ms: number) {
		return new Promise((resolve) => setTimeout(resolve, ms));
	}

	async function submitNote() {
		noteCopy = note;
		note = '';

		const condensedCategories = [];
		for (const category of Object.keys(categories)) {
			for (const subcategory of Object.keys(categories[category])) {
				condensedCategories.push(`${subcategory}_${category}`);
			}
		}

		noteProperties.set({ ...$noteProperties, topOffset: -70, leftPercOffset: 50, opacity: 1 });

		// Perform API request and get category
		const result = 'Personal_Goals';
		await sleep(1000);
		// console.log('submitting note...');
		// const result = await fetch('https://htn.onrender.com/categorize', {
		// 	method: 'POST',
		// 	headers: {
		// 		'Content-Type': 'application/json'
		// 	},
		// 	body: JSON.stringify({
		// 		categories: condensedCategories,
		// 		noteCopy
		// 	})
		// }).then((res) => {
		// 	console.log('res!', res);
		// 	return res.json();
		// });

		// console.log(result);
		// return;

		// Split result
		const [subcategoryResult, categoryResult] = result.split('_');

		// Animate adding note
		activeTab = categoryResult;
		await sleep(100);

		noteProperties.set({ ...$noteProperties, topOffset: -350 });

		categories[categoryResult][subcategoryResult].open = true;
		await sleep(300);

		categories[categoryResult][subcategoryResult].content = [
			...categories[categoryResult][subcategoryResult].content,
			noteCopy
		];

		noteProperties.set({ ...$noteProperties, opacity: 0 });
		await sleep(400);

		noteProperties.set({ leftPercOffset: 0, topOffset: 0, scale: 1, opacity: 0 });
	}
</script>

<div class="flex flex-col relative h-full">
	<div class="drop-shadow-md mb-2">
		<div class="bg-white py-2 w-full flex items-center justify-center">
			<img src="/logo.png" alt="Logo" style="height: 50px" />
		</div>
		<TabBar class="bg-white" tabs={['Tasks', 'Goals', 'Notes']} let:tab bind:active={activeTab}>
			<Tab {tab}>
				<Label>{tab}</Label>
			</Tab>
		</TabBar>
	</div>
	<div class="accordion-container">
		<Accordion>
			{#each Object.keys(categories[activeTab]) as subcategoryName}
				<SubcategoryPanel
					label={subcategoryName}
					content={categories[activeTab][subcategoryName].content}
					open={categories[activeTab][subcategoryName].open}
				/>
			{/each}
		</Accordion>
	</div>

	<div class="flex-1" />

	<div class="relative p-4 flex items-baseline gap-2 bg-gray-100">
		{#if $noteProperties.opacity > 0}
			<div
				style={`left: ${$noteProperties.leftPercOffset}%; transform: translate(-${$noteProperties.leftPercOffset}%, calc(-50% + ${$noteProperties.topOffset}px)) scale(${$noteProperties.scale}); opacity: ${$noteProperties.opacity}`}
				class="z-30 max-w-full absolute left-0 top-1/2 -translate-y-1/2"
			>
				<div
					class="mx-2 py-4 px-2 rounded-xl text-white bg-[#3499ff] whitespace-nowrap text-ellipsis overflow-hidden"
				>
					{noteCopy}
				</div>
			</div>
		{/if}

		<form on:submit={submitNote} class="w-full flex justify-end">
			<Input bind:value={note} class="solo-input" placeholder="Jot something down..." autofocus />
			<Button disabled={note.length === 0} type="submit">Submit</Button>
		</form>
	</div>
</div>

<style>
	* :global(.solo-input::placeholder) {
		color: var(--mdc-theme-on-surface, #000);
		opacity: 0.6;
	}
</style>

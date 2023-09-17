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
	const noteOffset = tweened({ x: 0, y: 0, scale: 1 }, { duration: 400, easing: cubicOut });
	async function submitNote() {
		const condensedCategories = [];
		for (const category of Object.keys(categories)) {
			for (const subcategory of Object.keys(categories[category])) {
				condensedCategories.push(`${subcategory}_${category}`);
			}
		}

		// Perform API request and get category
		const result = 'Personal_Goals';
		// console.log('submitting note...');
		// const result = await fetch('https://htn.onrender.com/categorize', {
		// 	method: 'POST',
		// 	headers: {
		// 		'Content-Type': 'application/json'
		// 	},
		// 	body: JSON.stringify({
		// 		categories: condensedCategories,
		// 		note
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

		setTimeout(() => {
			categories[categoryResult][subcategoryResult].open = true;
			setTimeout(() => {
				categories[categoryResult][subcategoryResult].content = [
					...categories[categoryResult][subcategoryResult].content,
					note
				];
				note = '';
			}, 300);
		}, 100);
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
		<!-- <div class="max-w-full absolute left-0 top-1/2 -translate-y-1/2">
			<div
				class="mx-2 py-4 px-2 rounded-xl text-white bg-[#3499ff] whitespace-nowrap text-ellipsis overflow-hidden"
			>
				{note}
			</div>
		</div> -->

		<Input bind:value={note} class="solo-input" placeholder="Jot something down..." autofocus />
		<Button disabled={note.length === 0} on:click={submitNote}>Submit</Button>
	</div>
</div>

<style>
	* :global(.solo-input::placeholder) {
		color: var(--mdc-theme-on-surface, #000);
		opacity: 0.6;
	}
</style>

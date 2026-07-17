export default function CommissioningStatusPage() {
  return (
    <main>
      <p className="eyebrow">Infrastructure commissioning</p>
      <h1>Web process ready</h1>
      <p>
        This smoke surface confirms that the UI shell starts. It contains no business data,
        workflow, or authenticated capability.
      </p>
      <dl>
        <div><dt>Surface</dt><dd>commissioning-status</dd></div>
        <div><dt>State</dt><dd>ready</dd></div>
      </dl>
    </main>
  );
}

/**
 * Project Chimera Command Center
 * End-to-End Governance Logic
 */

// Mock state management
const state = {
    pendingTasks: ['tsk-8821'],
    totalApproved: 0,
    totalRejected: 0
};

/**
 * Handle HITL approval/rejection actions
 * @param {string} taskId 
 * @param {string} action 
 */
function handleAction(taskId, action) {
    console.log(`[GOVERNANCE] Human ${action} for task: ${taskId}`);

    // Animate removal from queue
    const queue = document.getElementById('approval-queue');
    const items = queue.getElementsByClassName('approval-item');

    for (let item of items) {
        if (item.innerHTML.includes(taskId)) {
            item.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
            item.style.opacity = '0';
            item.style.transform = 'scale(0.9)';

            setTimeout(() => {
                item.remove();
                state.pendingTasks = state.pendingTasks.filter(id => id !== taskId);
                updateVisibility();
                showNotification(action);
            }, 300);
            break;
        }
    }
}

/**
 * Show feedback when a decision is made
 */
function showNotification(action) {
    const color = action === 'approve' ? '#48bb78' : '#f56565';
    const msg = action === 'approve' ? 'POST RATIFIED & PUBLISHED' : 'TRANSGRESSION REJECTED';

    const banner = document.createElement('div');
    banner.style.position = 'fixed';
    banner.style.top = '2rem';
    banner.style.right = '2rem';
    banner.style.background = color;
    banner.style.color = 'white';
    banner.style.padding = '1rem 2rem';
    banner.style.borderRadius = '8px';
    banner.style.fontWeight = '800';
    banner.style.boxShadow = '0 10px 30px rgba(0,0,0,0.5)';
    banner.style.zIndex = '1000';
    banner.innerText = msg;

    document.body.appendChild(banner);

    setTimeout(() => {
        banner.style.opacity = '0';
        banner.style.transition = 'opacity 1s ease';
        setTimeout(() => banner.remove(), 1000);
    }, 2000);
}

/**
 * Update empty state visibility
 */
function updateVisibility() {
    if (state.pendingTasks.length === 0) {
        document.getElementById('no-tasks').style.display = 'block';
    }
}

// Ensure the page is ready
window.onload = () => {
    console.log("PROJECT CHIMERA COMMAND CENTER INITIALIZED");
    console.log("PRIME DIRECTIVE: ACTIVE");
};
